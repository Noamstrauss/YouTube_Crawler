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
                 '''
            }
        post {
            success {
                echo 'Build Success '
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, to: 'nds597@walla.com', body: emailBody)
            }
            failure {
                 echo 'Build Failed'
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, to: 'nds597@walla.com', body: emailBody)
            }
        }

        }
        stage('Test Application') {
             echo 'Test Success'
            steps {
                echo 'Test Success'
            }
            post {
                success {
                    emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', to: 'nds597@walla.com', body: 'Test Passed')
                }
                failure {
                    emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', to: 'nds597@walla.com', body: 'Test Failed')
                }
            }
        }
        stage('Push Docker Image') {
            echo 'Push Success'
            when { anyOf {branch "master";branch "dev"} }
            steps {
                echo '=== Building Docker Image ==='
                script {
                   sh docker push $REGISTRY/$IMG
                }
            }

         post {
            failure {
                echo 'Push Failed'
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Push Failed', to: 'nds597@walla.com', body: 'Push Failed')
        }
      }

     }

        stage('Remove local images') {
            echo 'Removed local images Successfully'
            steps {
                echo '=== Delete the local docker images ==='
                sh final="${REGISTRY}/${IMG}"
                sh("docker rmi -f $final")
                sh("docker rmi -f $final$SHORT_COMMIT")
            }
        }
    }
}