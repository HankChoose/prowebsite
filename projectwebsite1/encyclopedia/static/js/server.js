const http = require("http");
const fs = require("fs");
const path = require("path");
const React = require("react");
const ReactDOMServer = require("react-dom/server");

function App(props) {
  return <h1>Hello, {props.name}!</h1>;
}

const server = http.createServer((req, res) => {
  const filePath = path.join(__dirname, "index.html");
  fs.readFile(filePath, "utf8", (err, html) => {
    if (err) {
      res.statusCode = 500;
      res.setHeader("Content-Type", "text/plain");
      res.end("Internal Server Error");
      console.error(err);
      return;
    }

    const reactHtml = ReactDOMServer.renderToString(<App name="World" />);
    const finalHtml = html.replace("{{react}}", reactHtml);

    res.statusCode = 200;
    res.setHeader("Content-Type", "text/html");
    res.end(finalHtml);
  });
});

server.listen(3000, () => {
  console.log("Server running at http://localhost:3000/");
});
