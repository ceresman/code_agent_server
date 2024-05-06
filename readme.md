# code agent server



## container launch example


```bash
docker run -it --gpus all -v /workspace:/workspace -v /data:/data -p 9999:9999 --name ele.ink.agent winshare/ele.ink:cn.cuda117.torch201.paddle251.nltk.codeagent.240327
```


## install &  server launch example

```bash
git clone https://github.com/ceresman/code_agent_server
cd code_agent_server
# server.py
uvicorn server:app --reload --host 0.0.0.0 --port 9999
```
