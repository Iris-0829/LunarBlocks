export default class Node {
    /**
     * Standard node in the command graph.
     * @param numPorts Number of input ports needed for this node to fully function.
     */
    constructor(numPorts){
        this.id = 0;
        this.numPorts = numPorts;
        this.params = [];
        this.terminals = [];
        this.outputs = [];
    }
    setId(id){
        this.id = id;
    }
}
