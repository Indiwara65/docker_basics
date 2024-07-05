# Undersatanding Github Actions           
* Github action is a platform that can be used to automate developer workflows such as  CI/CD workflow that allows to automate build, test and deployment.         
* In Github actions a workflow can be triggered when an event happens in the repo.           
* **Workflows**            
    * Workflow is a configurable automated process that will run one more jobs.              
    * A workflow can be triggerd by an *event* in the Github repo, manually or be scedulled.                 
    * Workflow is defined by using a **YAML** file in the .github/workflows directory in the repo.              
* **Event**      
    * Event is a specific action in the github repo that will trigger a workflow. eg - pull, push etc...              
* **Jobs**          
    * A job is a set of steps in a workflow that will be executed on the same runner.              
    * Jobs will be specified in the **YAML** file and will be run in that order.             
    * A job will be either a shell script or an action.      
    * Jobs in the same workflow can have dependecies, by default there are no dependencies.                 
    * Job eg :- Build, Test etc.. 
* **Action**                         
    * A reusable unit of code that performs a specific task, used within a job.
* **Runners**              
    * A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows; each workflow run executes in a fresh, newly-provisioned virtual machine.          

* Referance - https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

yaml - https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsuses