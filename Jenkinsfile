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
                 IMG="youtube_crawler:$BUILD_NUMBER"

                 echo 'Authentecating With ECS'
                 aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REGISTRY
                 echo '--------------------------------------'

                 echo '                                               '
                 echo 'B  u  i  l  d  i  n  g        D  o  c  k  e  r'
                 docker build -t $IMG .
                 echo '--------------------------------------'

                 echo '


                 '
                 echo '                                               '
                 echo 'S  e  t  t  i  n  g     A    T  a  g    T  o   4    T  h  e    D  o  c  k  e  r    I  m  a  g  e'
                 docker tag $IMG $REGISTRY/$IMG
                 echo '--------------------------------------'

                 echo '


                 '
                 echo '                                               '
                 echo 'P  u  s  h  i  n  g    T  h  e    I  m  a  g  e    T  o   E  C  R '
                 docker push $REGISTRY/$IMG
                 echo '--------------------------------------'


              '''
            }
        }
    }
  }
}
