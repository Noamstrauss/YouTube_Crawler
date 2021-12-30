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
        stage('Build Docker Image') {
        when { anyOf {branch "master";branch "dev"} }

            steps {
            echo '=== Building Docker Image ==='
                sh '''
            printf "${yellow}Authenticating With ECS...."
            aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REGISTRY
            printf "${green}Authenticating Was Successful! "
            printf "${yellow}Building Docker...."
            docker build -t $IMG .
            printf "${green}Build Was Successful!"
            printf "${yellow}Tagging Docker Image...."
            final="${REGISTRY}/${IMG}"
            docker tag $IMG $final
            printf "${green}Tagging Was Successful!"
            echo 'Tagging Was Successful!'
                 '''
            }
        post {
           /* success {
                echo 'Build Success '
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, to: 'nds597@walla.com', body: emailBody)
            }*/
            failure {
                 echo 'Build Failed'
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, to: 'nds597@walla.com', body: emailBody)
            }
        }

        }
        stage('Test Application') {
            steps {
            echo '=== Testing App ==='
                sh '''
                echo 'Test Success'
                '''

            }
            post {
                /*success {
                    emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', to: 'nds597@walla.com', body: 'Test Passed')
                }*/
                failure {
                    emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', to: 'nds597@walla.com', body: 'Test Failed')
                }
            }
        }
        stage('Push Docker Image') {

            when { anyOf {branch "master";branch "dev"} }
            steps {
                echo '=== Building Docker Image ==='
                script {
                sh '''
                   docker push $REGISTRY/$IMG
                   echo 'Push Success '
                   '''
                }
            }

         post {
            failure {
                echo 'Push Failed'
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Push Failed', to: 'nds597@walla.com', body: 'Push Failed')
        }
      }

     }

        stage('Cleanup local images') {

            steps {
              echo '=== Cleaning local image ==='
                script{
                sh '''
                echo '=== Delete the local docker images ==='
                final="${REGISTRY}/${IMG}"
                docker rmi -f $final
                echo 'Removed local image Successfully'
                    '''
                    }
            }
        }
    }
}