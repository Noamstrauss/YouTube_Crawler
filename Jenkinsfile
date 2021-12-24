    pipeline {
        agent any

  environment {
       REGISTRY = "955114013936.dkr.ecr.us-east-2.amazonaws.com"
       IMG="youtube_crawler:0.0.$BUILD_NUMBER"
       red="tput setaf 1"
       green="tput setaf 2"
               }

 stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            sh '''
            echo '***********************************************'
            echo '${red}A u t h e n t e c a t i n g   W i t h   E C S'
            echo '***********************************************'
            aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REGISTRY
            echo '***********************************************'
            echo '${green}A u t h e n t e c a t i o n   W a s   S u c c e s s f u l! '
            echo '***********************************************'
            echo '-----------------------------------------------'
            echo '***********************************************'
            echo '${red}B u i l d i n g    D o c k e r'
            echo '***********************************************'
            docker build -t $IMG .
            echo '***********************************************'
            echo '${green}S u c c e s s f u l l y  B u i l t  I m a g e ! '
            echo '***********************************************'
            echo '-----------------------------------------------'
            echo '***********************************************'
            echo '${red}T a g g i n g   D o c k e r   I m a g e'
            echo '***********************************************'
            docker tag $IMG $REGISTRY/$IMG
            echo '-----------------------------------------------'
            echo '***********************************************'
            echo '${red}P u s h i n g  T h e   I m a g e   T o  E C R '
            echo '***********************************************'
            docker push $REGISTRY/$IMG
            echo '-----------------------------------------------'
            echo '***********************************************'
            echo '${green}P u s h   W a s   S u c c e s s f u l! '
            echo '***********************************************'
            echo '-----------------------------------------------'
            '''
        }
    }
  }
}
