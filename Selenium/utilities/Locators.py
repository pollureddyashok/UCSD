
class Locator(object):
    
#LoginPage Locators
    
    BaseUrl = "https://172.31.234.59"
    Username_id = "//input[@id ='username']"
    Password_id = "//input[@id = 'password']"
    Login_id = "//input[@id = 'Submit']"
    
    
#Login Credentials

    Username = "admin"
    Password = "admin"
    
#Orchestration
    click_orchestration= "//a[normalize-space()='Orchestration']"
    Addworkflow= ".reportActionsToolbar .x-btn-default-toolbar-small:nth-of-type(1) [data-ref='btnIconEl']"
    Enter_workflowname= "//input[@data-custom-qtip='Workflow Name']"
    click_dropdown= ".x-anchor-form-item:nth-of-type(12) .x-form-arrow-trigger-default"
    Select_Apic= ".//li[@data-recordindex='1']"
    click_Next= ".primaryButton [data-ref='btnInnerEl']"
    link_text = "Next"
    clickNext= ".primaryButton [data-ref='btnInnerEl']"
    clik_Submit = ".primaryButton [data-ref='btnInnerEl']"
    
    
    
    
    workflow_name = "Test"