pipeline {
  agent any

  environment {
       REGISTRY = "955114013936.dkr.ecr.us-east-2.amazonaws.com"
       IMG="youtube_crawler:0.0.$BUILD_NUMBER"

  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            echo 'Starting to build docker image'
            script {
              sh '''
                 IMG="youtube_crawler:$BUILD_NUMBER"

                 echo 'Authentecating With ECS'
                 aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REGISTRY
                 echo '--------------------------------------'

                 echo '                                               '
                 echo '***********************************************'
                 echo 'B u i l d i n g    D o c k e r'
                 echo '***********************************************'
                 docker build -t $IMG .
                 echo '--------------------------------------'

                 echo '


                 '
                 echo '                                               '
                 echo '***********************************************'
                 echo 'S e t t i n g  A  T a g   T o  4   T h e   D o c k e r   I m a g e'
                 echo '***********************************************'
                 docker tag $IMG $REGISTRY/$IMG
                 echo '--------------------------------------'

                 echo '


                 '
                 echo '                                               '
                 echo '***********************************************'
                 echo 'P u s h i n g  T h e   I m a g e   T o  E C R '
                 echo '***********************************************'
                 docker push $REGISTRY/$IMG
                 echo '--------------------------------------'

                 echo '***********************************************'
                 echo 'P u s h   W a s   S u c c e s s f u l! '
                 echo '***********************************************'
              '''
            }
        }
    }
  }
}
