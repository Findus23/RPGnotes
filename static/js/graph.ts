import Sigma from "sigma";
import FA2Layout from 'graphology-layout-forceatlas2/worker';
import Graph from "graphology";
import random from 'graphology-layout/random';

const container = document.getElementById("graph")!

const graph = new Graph({
    type: "directed",
});



fetch('/graph/graph')
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
        graph.import(data)
        random.assign(graph);
        layout.start();
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


