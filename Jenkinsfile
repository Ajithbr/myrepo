// Jenkinsfile (Declarative Pipeline)
// Global Variable goes here
// Pipeline block
pipeline {
// Agent block
//agent {
//   node {
//      label 'Manage_Contact_Demo'
//   }
//}
agent any
options {
   buildDiscarder(logRotator(numToKeepStr: '5'))
   timestamps()
}
parameters {
   string(name: "Branch_Name", defaultValue: 'master', description: 'A name of the Git branch that contain the jenkinfile code')
   string(name: "Image_Name", defaultValue: 'manage_contact_app', description: 'A name of the image that you want to build')
   string(name: "Image_Tag", defaultValue: 'latest', description: 'Image tag')
   string(name: 'HTTP_PROXY', defaultValue: 'http://16.242.46.30:8080')
   string(name: 'HTTPS_PROXY', defaultValue: 'http://16.242.46.30:8080')
   
   booleanParam(name: "PushImage", defaultValue: false)
}
// Stage Block
stages {// stage blocks
   stage("Build docker images") {
      steps {
         script {
            echo "Bulding docker images"
            def buildArgs = """\
--build-arg HTTP_PROXY=${params.HTTP_PROXY} \
--build-arg HTTPS_PROXY=${params.HTTPS_PROXY} \
-f Dockerfile \
."""
            docker.build("${params.Image_Name}:${params.Image_Tag}", buildArgs)
         }
     }
}
stage("Push to Dockerhub") {
   when {
      equals expected: "true", actual: "${params.PushImage}"
   }
   steps {
      script {
         echo "Pushing the image to docker hub"
         def localImage = "${params.Image_Name}:${params.Image_Tag}"
         def repositoryName = "ajhebtr/${localImage}"
         sh "docker tag ${localImage} ${repositoryName} "
         docker.withRegistry("", "DockerHubCredentials") {
            def image = docker.image("${repositoryName}");
            image.push()
         }
     }
  }
}}
post {
   always {
      script {
         echo "I am execute always"
      }
   }
   success {
      script {
         echo "I am execute on success"
      }
   }
   failure {
      script {
         echo "I am execute on failure"
      }
   }
}}
