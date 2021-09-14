t3flow_def = {
  "Comment": "A workflow to transfer data into HPC, train a DL model with the data and transfer trained model back",
  "StartAt": "TransferData",
  "States": {
    "TransferData": {
      "Comment": "Transfer data of diffraction pattern",
      "Type": "Action",
      "ActionUrl": "https://actions.automate.globus.org/transfer/transfer",
      "ActionScope": "https://auth.globus.org/scopes/actions.globus.org/transfer/transfer",
      "Parameters": {
        "source_endpoint_id.$": "$.input.data_endpoint", 
        "destination_endpoint_id.$": "$.input.comp_endpoint",
        "encrypt_data": False,
        "transfer_items": [
          {
            "source_path.$": "$.input.data_path",
            "destination_path.$": "$.input.comp_path",
            "recursive": True
          }
        ]
      },
      "ResultPath": "$.result_path",
      "WaitTime": 600,
      "Next": "TrainModel"
    },
    "TrainModel": {
      "Comment": "Run the funcX function to train BraggNN",
      "Type": "Action",
      "ActionUrl": "https://automate.funcx.org",
      "ActionScope": "https://auth.globus.org/scopes/b3db7e59-a6f1-4947-95c2-59d6b7a70f8c/action_all",
      "Parameters": {
          "tasks": [{
            "endpoint.$": "$.input.fx_ep",
            "function.$": "$.input.fx_id",
            "payload.$": "$.input.params"
        }]
      },
      "ResultPath": "$.result_path",
      "WaitTime": 1800,
      "Next": "TransferModel"
    },
    "TransferModel": {
      "Comment": "Return transfer to move model back",
      "Type": "Action",
      "ActionUrl": "https://actions.automate.globus.org/transfer/transfer",
      "ActionScope": "https://auth.globus.org/scopes/actions.globus.org/transfer/transfer",
      "Parameters": {
        "source_endpoint_id.$": "$.input.comp_endpoint", 
        "destination_endpoint_id.$": "$.input.dest_endpoint",
        "encrypt_data": False,
        "transfer_items": [
          {
            "source_path.$": "$.input.mdl_path",
            "destination_path.$": "$.input.dest_path",
            "recursive": True 
          }
        ]
      },
      "ResultPath": "$.TransferModelRes",
      "WaitTime": 600,
      "End": True
    },
  }
}