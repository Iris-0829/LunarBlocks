import InNode from 'InNode.js';
import OutNode from 'OutNode.js';

export default class GraphState {
    /**
     * The graph used for computing its output.
     */
    constructor(){
        this.inNode = null;
        this.outNode = null;
        this.operatorNodes = [];
    }
    setIn(numPorts, terminals){
        /**
         * Adds input node to the graph with the given numPorts
         * @param {int} numPorts Number of ports in the input node.
         */
        this.inNode = new InNode(numPorts);
        this.inNode.terminals = terminals; // should be the same length
    }
    setOut(numPorts){
        /**
         * Adds output node to the graph with the given numPorts
         * @param {int} numPorts Number of ports in the output node.
         */
        this.outNode = new OutNode(numPorts);
    }
    addOperator(operatorNode){
        /**
         * Adds operator to the graph.
         * @param {OperatorNode} operatorNode The operatorNode to add to the graph.
         */
        this.operatorNodes.push(operatorNode);
    }
    removeOperator(operatorNode){
        /**
         * Removes operatorNode as a terminal.
         * @param {OperatorNode} operatorNode The operatorNode to remove from the graph.
         */

        // get rid of all connections to it first
        for (let i = 0; i < this.operatorNodes.length; i++){
            this.operatorNodes[i].removeTerminal(operatorNode);

            // get rid of the node itself
            if (this.operatorNodes[i] === operatorNode){
                this.operatorNodes.splice(i, 1);
            }
        }
    }
}
