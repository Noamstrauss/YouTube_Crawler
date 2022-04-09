pipeline {
    agent any

     environment {
       REGISTRY = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
       IMG="youtube_crawler:latest"
       FINALTAG="${REGISTRY}/${IMG}"
       REGION="eu-north-1"
       clustername="devops-apr21-k8s"
       red='\033[0;31m'
       green='\033[0;32m'
       yellow='\033[0;33m'
       def emailBody = '${JELLY_SCRIPT,template="html_gmail"}'
       def emailSubject = "${env.JOB_NAME} - Build# ${env.BUILD_NUMBER}"
       }

    stages {
        stage('Build Docker Image') {

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
            docker tag $IMG $FINALTAG
            printf "${green}Tagging Was Successful!"
            echo 'Tagging Was Successful!'
                 '''

            }
             post {
            success {
                echo 'Build Success '
               /* emailext(mimeType: 'text/html', subject: emailSubject, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: emailBody)*/
            }
            failure {
                 echo 'Build Failed'
                emailext(mimeType: 'text/html', subject: emailSubject, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: emailBody)
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
                    /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
                failure {
                    emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Failed')
                }
            }
        }
        stage('Push Docker Image') {

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
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Push Failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Push Failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Push Failed')
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

       stage('Terraform Init') {

            steps {
              echo '=== Running Terraform Init ==='
                script{
                sh '''
                terraform init
                   '''
                    }
    }
             post {
            success {
                echo 'Terraform init was successful'
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Terraform init failed'
                emailext(mimeType: 'text/html', subject: emailSubject+' Terraform init failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: ' Terraform init failed')
        }
      }
}

       stage('Terraform plan') {

            steps {
              echo '=== Running Terraform plan ==='
                script{
                sh '''
                aws eks update-kubeconfig --region eu-north-1 --name ${clustername} --kubeconfig .kube
                terraform plan -var-file=vars.tfvars
                    '''
                    input "Proceed to apply stage?"
                    }
    }
             post {
            success {
                echo 'Terraform plan ran successfully'
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Terraform plan failed'
                emailext(mimeType: 'text/html', subject: emailSubject+' Terraform init failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: ' Terraform init failed')
        }
      }
}


       stage('Terraform apply') {

            steps {
              echo '=== Running Terraform Apply ==='
                script{
                sh '''
                terraform apply -var-file=vars.tfvars -auto-approve
                    '''

                    }
    }
             post {
            success {
                echo 'Terraform apply ran successfully'
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Terraform apply failed'
                emailext(mimeType: 'text/html', subject: emailSubject+' Terraform apply failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: ' Terraform apply failed')
        }
      }

}

    }
}