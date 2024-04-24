import azure.functions as func
import logging

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="myqueue",
                               connection="6aec35_STORAGE") 
@app.blob_output(arg_name="outblob", path="outcontainer/out.txt",
                               connection="6aec35_STORAGE")
def queue_trigger(azqueue: func.QueueMessage, outblob: func.Out[str]):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))
