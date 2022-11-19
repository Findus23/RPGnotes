import Sigma from "sigma";
import ForceSupervisor from "graphology-layout-force/worker";
import Graph from "graphology";
import random from 'graphology-layout/random';

const container = document.getElementById("graph")
console.log("graph")
if (container) {
    const graph = new Graph({
        type: "directed",
    });
    //
    // graph.addNode("John", {x: 0, y: 10, size: 50, label: "John", color: "blue"});
    // graph.addNode("Mary", {x: 10, y: 0, size: 30, label: "Mary", color: "red"});
    // graph.addNode("test", {x: 10, y: 10, size: 30, label: "Mary", color: "red"});
    // graph.addNode("test2", {x: 10, y: 100, size: 30, label: "Mary", color: "red"});
    //
    // graph.addEdge("John", "Mary");
    // graph.addEdge("John", "test");
    // graph.addEdge("Mary", "test");
    // graph.addEdge("Mary", "test2");

    fetch('/graph/graph')
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            graph.import(data)
            random.assign(graph);
        });


    // Create the spring layout and start it
    const layout = new ForceSupervisor(graph, {isNodeFixed: (_, attr) => attr.highlighted});
    layout.start();

    console.log(graph.export())


// eslint-disable-next-line @typescript-eslint/no-unused-vars
    const renderer = new Sigma(graph, container, {
        labelSize: 20,
        edgeLabelSize: 200,
    });
}


