# Ask Your Prof

> Active Development. The current version is **NOT** stable. It generally runs, but there are some issues with the OpenAI API, although that could also just be a misconfiguration of my API key, to be honest. This was a fun little side project of mine where I wanted to try out LangChain's new [LCEL](https://blog.langchain.dev/langchain-expression-language/). Also, it is more or less a generalization of a private RAG chatbot that I created to study for one of my university courses by running it on my professor's lectures and slides.

Your personal AI professor having access to lecture recordings, slides and notes.

![CleanShot 2023-12-28 at 00 15 05@2x](https://github.com/marcjulianschwarz/ask-your-prof/assets/67844154/ae468092-765f-47d1-bce2-687d7ba9a81e)

## How to use

### Backend

Install all packages with `pip install -r requirements.txt`, install profai with `pip install -e .` and run the backend by executing `flaks run` in the backend folder.

### Frontend

Install all packages with `npm install` and then run it with `npm run dev`. The app will run on `localhost:5173`.
