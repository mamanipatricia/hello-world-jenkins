
pipeline {
    // agent { docker { image 'python:3.10.1-alpine' } }
    agent any
    parameters {
        string(name: 'repoName', description: 'Type Helm Repo Name to list the artifacts to remove', defaultValue: 'xtime-helm-local')
        string(name: 'itemName', description: 'Type Helm Item Name to remove', defaultValue: 'consumer' )
    }

    stages {
        stage('List_Helm_artifacts_to_remove') {
            when {
                expression { params.repoName != '' && params.itemName != '' }
            }
            steps {
                script {
                    timeout(time: 10, unit: "MINUTES") {
                        input message: 'Do you want to remove the artifacts?', ok: 'Yes'
                    }

                    sh "ls"
                    sh "pwd"
                    sh "./test.sh"
                    // sh "/usr/local/bin/python --version"
                    // sh "pip install requests"
                    // def cmdArray = ["python", "./remove-artifacts.py", params.repoName, params.itemName, env.ARTIFACTORY_API_KEY]
                    // def proc = cmdArray.execute()
                    // proc.waitFor()
                    // println "finished...!"
                    // println "return code: ${ proc.exitValue()}"
                    // println "stderr: ${proc.err.text}"
                    // println "stdout: ${proc.in.text}"
                }
            }
        }

    }
}

// timeout(time: 2, unit: “HOURS”) {
//     input message: ‘Approve Deploy?’, ok: ‘Yes’
// }


// pipeline {
//     agent { docker { image 'python:3.10.1-alpine' } }
//     stages {
//         stage('build') {
//             steps {
//                 sh 'python --version'
//             }
//         }
//     }
// }
// https://github.com/jenkinsci/docker/blob/master/README.md