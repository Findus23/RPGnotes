import Sigma from "sigma";
import FA2Layout from 'graphology-layout-forceatlas2/worker';
import Graph from "graphology";
import random from 'graphology-layout/random';

const container = document.getElementById("graph")!

const graph = new Graph({
    type: "directed",
});


fetch('http://localhost:8080')
    .then((response) => response.json())
    .then((a) => new Promise(resolve => setTimeout(resolve, 1000, a)))
    .then((data) => {
        console.log(data)
        graph.import(data)
        random.assign(graph);
        layout.start();
        window.setInterval(function(){
        console.info(layout.isRunning())
}, 500);
    });


const layout = new FA2Layout(graph, {
    settings: {
        gravity: 0.2
    }
});


const renderer = new Sigma(graph, container, {
    labelSize: 20,
    edgeLabelSize: 200,
});


renderer.on("clickNode", (e) => {
    const url = graph.getNodeAttribute(e.node, "url")
    window.open(url, 'graphURL')

})


