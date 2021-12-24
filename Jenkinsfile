    pipeline {
        agent any

  environment {
       REGISTRY = "955114013936.dkr.ecr.us-east-2.amazonaws.com"
       IMG="youtube_crawler:0.0.$BUILD_NUMBER"
       red='\033[0;31m'
       green='\033[0;32m'
       yellow='\033[0;33m'
       EMAIL_TO = 'nds597@walla.com'
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
             echo 'Build Was Successful'
             emailext body: 'Check console output at $BUILD_URL to view the results. \n\n ${CHANGES} \n\n -------------------------------------------------- \n${BUILD_LOG, maxLines=100, escapeHtml=false}',
                    to: "${EMAIL_TO}",
                    subject: 'Build Successful in Jenkins: $PROJECT_NAME - #$BUILD_NUMBER'
         }
         failure {
             mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: 'nds597@walla.com', mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "nds597@walla.com";
         }
     }
 }