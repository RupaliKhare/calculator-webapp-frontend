pipeline {
    environment {
    imagename = "frontend"
    jenkinsProject = 'calculator-webapp-backend'
  }

    agent any
    stages {

        stage('Git Staging'){

            steps{

                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-cred', url: 'https://github.com/RupaliKhare/calculator-webapp-frontend.git']]])

            }
        }


        stage('Build image and Run image ') {

            steps{
                sh 'sudo su - jenkins -s/bin/bash'
                //sh 'sudo docker stop $imagename'
                //sh 'sudo docker rm $imagename'
                //sh 'sudo docker rmi $imagename'
                sh 'sudo docker image build -t  $imagename .'

            }

        }
        
        stage('Run image ') {

            steps{
                sh 'sudo docker run -p5001:5001 --restart=always --name $imagename  -itd $imagename'

            }

        }
        

        
    }
}
