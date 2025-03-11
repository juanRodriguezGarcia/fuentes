
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  KnowledgeBaseWithAOSS:
    Type: AWS::Bedrock::KnowledgeBase
    Properties:
      Name: "MiKnowledgeBase"
      Description: "Knowledge Base con OpenSearch Serverless"
      RoleArn: !Ref AmazonBedrockExecutionRole
      KnowledgeBaseConfiguration:
        Type: "VECTOR"
        VectorKnowledgeBaseConfiguration:
          EmbeddingModelArn: !Sub "arn:${AWS::Partition}:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v2"
      StorageConfiguration:
        Type: "OPENSEARCH_SERVERLESS"
        OpensearchServerlessConfiguration:
          CollectionArn: !Ref CollectionArn
          VectorIndexName: "my-vector-index"
          FieldMapping:
            VectorField: "vector"
            TextField: "text"
            MetadataField: "metadata"

  AmazonBedrockExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: "BedrockExecutionRole"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service: "bedrock.amazonaws.com"
            Action: "sts:AssumeRole"
      Policies:
        - PolicyName: "BedrockOpenSearchPolicy"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: "Allow"
                Action:
                  - "aoss:APIAccessAll"
                  - "aoss:ListCollections"
                  - "aoss:ListIndexes"
                  - "aoss:ReadDocument"
                  - "aoss:WriteDocument"
                Resource: "*"

  CollectionArn:
    Type: AWS::SSM::Parameter
    Properties:
      Name: "/opensearch-serverless/collection-arn"
      Type: String
      Value: "arn:aws:aoss:us-east-1:123456789012:collection/my-collection"


      aws bedrock-agent start-ingestion-job \
  --knowledge-base-id <KnowledgeBaseId> \
  --data-source-id <DataSourceId>


      FoundationModel: "anthropic.claude-3.5-sonnet-20240229-v1:0"

aws bedrock-agent create-agent-version --agent-id "ID_DE_TU_AGENTE" --description "Segunda versión del agente"

aws bedrock update-agent-alias  --agent-id "ID_DE_TU_AGENTE"  --alias-name "NOMBRE_DEL_ALIAS" --description "Descripción del alias"  --routing-configuration "{"createNewVersion": true}"




        stage('Setup Parameters') {
            steps {
                script {
                    properties([
                        parameters([
                            string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'Especifica el entorno de despliegue'),
                            booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Ejecutar pruebas antes de desplegar'),
                            choice(name: 'DEPLOY_REGION', choices: ['us-east-1', 'us-west-2', 'eu-central-1'], description: 'Región de despliegue')
                        ])
                    ])
                }
            }
        }

