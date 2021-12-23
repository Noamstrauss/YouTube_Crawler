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

                 echo '--------------------------------------'

                 echo 'Building Docker'

                 docker build -t youtube_crawler:$BUILD_NUMBER .

                 echo '--------------------------------------'

                 echo 'Setting A Tag To The Docker Image'
                 docker tag youtube_crawler:$BUILD_NUMBER $REGISTRY/youtube_crawler:$BUILD_NUMBER

                 echo '--------------------------------------'

                 echo 'Pushing The Image To ECR'
                 docker push $REGISTRY/youtube_crawler:$BUILD_NUMBER
                 docker push $REGISTRY/youtube_crawler:$BUILD_NUMBER



                 echo '--------------------------------------'


              '''
            }
        }
    }
  }
}
