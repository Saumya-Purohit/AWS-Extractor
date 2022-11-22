 # change LINE by WORD if you want word level extraction
        raw_text = extract_text(response, extract_by="LINE")
        print(raw_text)
        s3 = boto3.client("s3")
        bucket = "sjcomprehendbucket"
        with open("/tmp/raw_text.txt", "w") as f:
            f.write(str(raw_text))
        client = boto3.resource("s3")
        client.meta.client.upload_file("/tmp/raw_text.txt", bucket, "raw_text.txt")


        return {
            "statusCode": 200,
            "body": json.dumps("Document processed successfully!"),
        }
    
    return {"statusCode": 500, "body": json.dumps("There is an issue!")}




