# jenkins notes

resource: https://www.youtube.com/watch?v=7KCS70sCoK0

Jenkinsfile can be written as a
1. scripted pipeline or
2. a declarative pipeline

1. Scripted pipeline: was the first syntax of jenkins file -> aalows to write the whole configuration of the Jenkins file using Groovy script...
- first syntax
- groovy engine

example:

node {
    // groovy script
}

2. Declarative syntax
- you are not limited in a ny way but it's easier to get started because you have a predefined structure you have to follow and fill in the gaps

example:

```groovy=
pipeline {
    agent any

    stages {

        stage("build") {
            steps {
                // ....
            }
        }
    }
}

node {
    // groovy script
}
```

Explanation:

- pipeline: you declare a pipeline - (must be top-level)
- agent: any agent - (where to execute) this build is gonna on any available Jenkins agent an
an agent can be a node or note?, or it could be executors on that node or note?.
An agent is more relevant when you have a Jenkins cluster with *master* and *slaves* where you have
Windows nodes and Linux nodes, etc

agent any => we will run with the next available agent.

pipeline and agent any ARE EQUIVALENT and requiered attributes you always have to use them

- stages: wherethe whole work actually happens (where the "work" happens) we have different stages of that pipeline

Inside stages we define stage name and we can define as many stages as we want..

example:

pipeline {
    agent any

    stages {

        stage("build") {
            steps {
                // ....
            }
        }

         stage("test") {
            steps {
                // ....
            }
        }

         stage("deploy") {
            steps {
                // ....
            }
        }
    }
}

stages
- chekout
- cleanup
- build
- test
- deploy


then inside goes the script that actually executes some comments on the Jenkins server o Jenkins agent

exmaple with JS

pipeline {
    agent any

    stages {

        stage("build") {
            steps {
                sh "npm install"
                sh "npm build"
            }
        }

        stage("build") {
            steps {
                echo "building the application..."
            }
        }
        ...
    }
}
