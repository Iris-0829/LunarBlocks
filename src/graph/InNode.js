import Node from 'Node.js';

export default class InNode extends Node{
    /**
     * Handles operands input into the graph.
     * @param {int} numPorts Number of input ports the InNode can take.
     */
    constructor(numPorts){
        super(numPorts);
    }
    advance(){
        /**
         * Moves operands to their designated terminals.
         */
        for (let i = 0; i < this.numPorts; i++){
            for (let j = 0; j < this.params[i]; j++) {
                this.terminals[i].addParams(this.params[i][j]);
            }
        }
    }
}
