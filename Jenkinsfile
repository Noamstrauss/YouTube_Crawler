    pipeline {
        agent any

  environment {
       REGISTRY = "955114013936.dkr.ecr.us-east-2.amazonaws.com"
       IMG="youtube_crawler:0.0.$BUILD_NUMBER"
       red='\033[0;31m'
       green='\033[0;32m'
       yellow='\033[0;33m'
       def emailBody = '${JELLY_SCRIPT,template="html_gmail"}'
       def emailSubject = "${env.JOB_NAME} - Build# ${env.BUILD_NUMBER}"
       }

 stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            sh '''
            printf "***********************************************"
            printf "${yellow}A u t h e n t e c a t i n g   W i t h   E C S...."
            printf "***********************************************"
            aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REGISTRY
            printf "***********************************************"
            printf "${green}A u t h e n t e c a t i o n   W a s   S u c c e s s f u l! "
            printf "***********************************************"
            printf "                                               "
            printf "                                               "
            printf "***********************************************"
            printf "${yellow}B u i l d i n g    D o c k e r...."
            printf "***********************************************"
            docker build -t $IMG .
            printf "***********************************************"
            printf "${green}S u c c e s s f u l l y  B u i l t  I m a g e ! "
            printf "***********************************************"
            printf "                                               "
            printf "                                               "
            printf "***********************************************"
            printf "${yellow}T a g g i n g   D o c k e r   I m a g e....."
            printf "***********************************************"
            docker tag $IMG $REGISTRY/$IMG
            printf "***********************************************"
            printf "${green}T a g g e d  I m a g e! "
            printf "***********************************************"
            printf "                                               "
            printf "                                               "
            printf "${yellow}P u s h i n g  T h e   I m a g e   T o  E C R.... "
            printf "***********************************************"
            docker push $REGISTRY/$IMG
            printf "***********************************************"
            printf "${green}P u s h   W a s   S u c c e s s f u l! "
            printf "***********************************************"
            printf "                                               "
            '''
                        }
                    }
                  }
      post {
        success {
            echo 'Build Success'
            emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, to: 'nds597@walla.com', body: emailBody)
        }
        failure {
            echo 'Build Failed'
            emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, to: 'nds597@walla.com', body: emailBody)
        }
    }
 }