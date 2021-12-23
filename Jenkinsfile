pipeline {
  agent any

  environment {
       REGISTRY = "955114013936.dkr.ecr.us-east-2.amazonaws.com"
  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            echo 'Starting to build docker image'
            script {
              sh '''

                 echo 'Authentecating With ECS'
                 aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REGISTRY
                 echo 'Building Docker'
                 docker build -t youtube_crawler .
                 echo 'Setting A Tag To The Docker Image'
                 docker tag youtube_crawler:1.0 $REGISTRY/youtube_crawler:1.0
                 echo 'Pushing The Image To ECR'
                 docker push 955114013936.dkr.ecr.us-east-2.amazonaws.com/youtube_crawler:latest


              '''
            }
        }
    }
  }
}
