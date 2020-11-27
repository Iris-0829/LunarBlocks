import Node from 'Node.js';

export default class OutNode extends Node{
    /**
     * Last node that stores the graph's output.
     * @param {int} numPorts Number of input ports the OutNode can take.
     */
    constructor(numPorts){
        super(numPorts);
    }
    addParams(operand){
        /**
         * Adds operand to output.
         * @param {Operand} operand Operand to add to output.
         */
        if (this.params.length < this.numPorts) {
            this.params.push(operand);
        }
    }
    execute(){
        /**
         * Returns output.
         */
        return this.params;
    }
}
