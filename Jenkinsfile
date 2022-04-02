pipeline {
    agent any

     environment {
       REGISTRY = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
       IMG="youtube_crawler:0.0.$BUILD_NUMBER"
       FINALTAG=${REGISTRY}/${IMG}
       REGION="eu-north-1"
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
            echo '=== Building Docker Image  ==='
                sh '''
            printf "${yellow}Authenticating With ECS...."
            aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $REGISTRY
            printf "${green}Authenticating Was Successful! "
            printf "${yellow}Building Docker...."
            docker build -t $IMG .
            printf "${green}Build Was Successful!"
            printf "${yellow}Tagging Docker Image...."
            final= ${REGISTRY}/${IMG}
            docker tag $IMG $final
            printf "${green}Tagging Was Successful!"
            echo 'Tagging Was Successful!'
                 '''

            }
        post {
            success {
                echo 'Build Success '
               /* emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: emailBody)*/
            }
            failure {
                 echo 'Build Failed'
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: emailBody)
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
                success {
                  echo 'Test Success '
                    /*emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
                failure {
                    emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Failed')
                }
            }
        }
        stage('Push Docker Image') {

            when { anyOf {branch "master";branch "dev"} }
            steps {
                echo '=== Building Docker Image ==='
                script {
                sh '''
                   docker push $FINALTAG
                   echo 'Push Success '
                   '''
                }
            }

         post {
         success {
                echo 'Push Success '
                /*emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Push Failed'
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Push Failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Push Failed')
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
                docker system prune -f
                echo 'Removed local image Successfully'
                    '''
                    }
            }
        }
        stage('Grafana Deployment') {

            steps {
              echo '=== Starting deployment ==='
                script{
                sh '''
                cd infra/grafana
                terraform apply -var-file=vars.tfvars -auto-approve
                echo 'Deployment was success'
                    '''
                    }
    }
             post {
         success {
                echo 'Grafana Deploy was successful '
                /*emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Grafana Deployment failed'
                emailext(mimeType: 'text/html', replyTo: 'nds597@walla.com', subject: emailSubject+'grafana deploy failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'grafana deploy failed')
        }
      }
}

    }
}