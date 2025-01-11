import Sigma from "sigma";
import FA2Layout from 'graphology-layout-forceatlas2/worker';
import Graph from "graphology";
import random from 'graphology-layout/random';
import forceAtlas2 from "graphology-layout-forceatlas2";

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
        const sensibleSettings = forceAtlas2.inferSettings(graph);
        console.log(sensibleSettings);
        layout.start();
    });

const urlParams = new URLSearchParams(window.location.search);


function parseBool(value: string | null): boolean {
    return value?.toLowerCase() === "true";
}

const layout = new FA2Layout(graph, {
    settings: {
        gravity: parseFloat(urlParams.get("gravity") || "0.05"),
        strongGravityMode: parseBool(urlParams.get("strongGravityMode") || "true"),
        slowDown: parseFloat(urlParams.get("gravity") || "5.4"),
        scalingRatio: parseFloat(urlParams.get("scalingRatio") || "10")
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


