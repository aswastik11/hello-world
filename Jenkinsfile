pipeline{
    agent any
    
    stages{
        stage('Clone Code') {
            steps {
                git url:'https://github.com/aswastik11/hello-world.git', branch: "develop"
            }
        }
        stage("Code Build & Test"){
            steps{
                echo "Code Build Stage"
                sh "docker build -t hello-world ."
            }
        }
        stage("Build Image and Push"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"dockerHubCred",
                    usernameVariable:"dockerHubUser", 
                    passwordVariable:"dockerHubPass")]){
                sh 'echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin'
                sh "docker image tag hello-world:latest ${env.dockerHubUser}/hello-world:latest"
                sh "docker push ${env.dockerHubUser}/hello-world:latest"
                }
            }
        }
    }
}
