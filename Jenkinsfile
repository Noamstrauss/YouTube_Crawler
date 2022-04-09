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

       stage('Terraform state Infra') {

            steps {
              echo '=== Running Terraform Init ==='
                script{
                sh '''
                cd infra/s3
                terraform init
                echo '=== Running Terraform plan ==='
                terraform plan
                echo '=== Running Terraform apply ==='
                terraform apply -auto-approve
                    '''
                    }
    }
             post {
         success {
                echo 'Terraform state Infra was successfully set'
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Terraform state Infra infrastructure failed'
                emailext(mimeType: 'text/html', subject: emailSubject+' Terraform state infrastructure setup failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: ' Terraform state infrastructure setup failed')
        }
      }
}

       stage('Grafana Infrastructure ') {

            steps {
              echo '=== Running Terraform Init ==='
                script{
                sh '''
                cd infra/grafana
                terraform init
                    '''
                    }
    }
             post {
         success {
                echo 'Terraform init ran successfully'
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Terraform init failed'
                emailext(mimeType: 'text/html', subject: emailSubject+' Terraform init failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: ' Terraform init failed')
        }
      }
}


       stage('Grafana Terraform Plan') {

            steps {
              echo '=== Running Terraform Plan ==='
                script{
                sh '''
                cd infra/grafana
                aws eks update-kubeconfig --region eu-north-1 --name ${clustername} --kubeconfig .kube
                terraform plan -var-file=vars.tfvars
                    '''

                    }
    }
}

        stage('Grafana Terraform Apply') {

            steps {
              echo '=== Starting Terraform Apply ==='
                script{
                sh '''
                cd infra/grafana

                terraform apply -var-file=vars.tfvars -auto-approve
                    '''
                    }
    }
             post {
         success {
                echo 'Terraform Apply was successful '
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Terraform Apply failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Terraform Apply failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Terraform Apply failed')
        }
      }
}
        stage('Youtube-App FRONT Terraform Init') {

            steps {
              echo '=== Starting Terraform Init ==='
                script{
                sh '''
                cd infra/youtube-frontend

                terraform init
                    '''
                    }
    }
             post {
         success {
                echo 'Youtube-App FRONT Terraform Init was successful '
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Youtube-App FRONT Terraform Init failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Youtube-App FRONT Terraform Init failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Youtube-App FRONT Terraform Init failed')
        }
      }
}


 stage('Youtube-App FRONT Terraform plan') {

            steps {
              echo '=== Starting Terraform Plan ==='
                script{
                sh '''
                cd infra/youtube-frontend
                aws eks update-kubeconfig --region eu-north-1 --name ${clustername} --kubeconfig .kube
                terraform plan -var-file=vars.tfvars
                    '''
                   input "Proceed to apply stage?"
                    }
    }
             post {
            success {
                echo 'Youtube-App FRONT Terraform plan was successful '
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Youtube-App FRONT Terraform plan failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Youtube-App FRONT Terraform plan failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Youtube-App FRONT Terraform plan failed')
        }
      }
}

 stage('Youtube-App FRONT Terraform Apply') {

            steps {
              echo '=== Starting Terraform Apply ==='
                script{
                sh '''
                cd infra/youtube-frontend
                terraform apply -var-file=vars.tfvars -auto-approve
                    '''
                    }
    }
             post {
            success {
                echo 'Youtube-App FRONT Terraform Apply was successful '
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Youtube-App FRONT Terraform Apply failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Youtube-App FRONT Terraform Apply failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Youtube-App FRONT Terraform Apply failed')
        }
      }
}
        stage('Youtube-App BACK Terraform Init') {

            steps {
              echo '=== Starting Terraform Init ==='
                script{
                sh '''
                cd infra/youtube-backend
                terraform init
                    '''
                    }
    }
             post {
         success {
                echo 'Youtube-App BACK Terraform Init was successful '
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Youtube-App BACK Terraform Init failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Youtube-App BACK Terraform Init failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Youtube-App BACK Terraform Init failed')
        }
      }
}


 stage('Youtube-App BACK Terraform plan') {

            steps {
              echo '=== Starting Terraform Plan ==='
                script{
                sh '''
                cd infra/youtube-backend
                aws eks update-kubeconfig --region eu-north-1 --name ${clustername} --kubeconfig .kube
                terraform plan -var-file=vars.tfvars
                    '''
                   input "Proceed to apply stage?"
                    }
    }
             post {
            success {
                echo 'Youtube-App BACK Terraform plan was successful '
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Youtube-App BACK Terraform plan failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Youtube-App BACK Terraform plan failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Youtube-App BACK Terraform plan failed')
        }
      }
}

 stage('Youtube-App BACK Terraform Apply') {

            steps {
              echo '=== Starting Terraform Apply ==='
                script{
                sh '''
                cd infra/youtube-backend
                terraform apply -var-file=vars.tfvars -auto-approve
                    '''
                    }
    }
             post {
            success {
                echo 'Youtube-App BACK Terraform Apply was successful '
                /*emailext(mimeType: 'text/html', subject: emailSubject+'Test Results', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Test Passed')*/
                }
            failure {
                echo 'Youtube-App BACK Terraform Apply failed'
                emailext(mimeType: 'text/html', subject: emailSubject+'Youtube-App BACK Terraform Apply failed', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], body: 'Youtube-App BACK Terraform Apply failed')
        }
      }
}


    }
}