import Node from 'Node.js';

export default class OperatorNode extends Node{
    /**
     * Node in the graph.
     * @param {int} numPorts Number of input ports the Node can take.
     */
    constructor(numPorts){
        super(numPorts);
    }
    addParams(operand){
        /**
         * Adds operand as a parameter to the operator. Return true if it passes, false otherwise.
         * @param {Operand} operand Operand to add to output.
         */
        if (this.params.length < this.numPorts) {
            this.params.push(operand);
            return true;
        } else {
            return false;
        }
    }
    addTerminal(operatorNode){
        /**
         * Adds operatorNode as a terminal to the operator.
         * @param {OperatorNode} operatorNode Where the output is going to go when advanced.
         */
        this.terminals.push(operatorNode);
    }
    removeTerminal(operatorNode){
        /**
         * Removes operatorNode as a terminal.
         * @param {OperatorNode} operatorNode The operatorNode to remove from the list of terminals.
         */
        const i = this.inTerminal(operatorNode);
        if (i !== -1){
            this.terminals.splice(i, 1);
        }
    }
    inTerminal(operatorNode){
        /**
         * Checks whether the operator node is listed as a terminal.
         * @param {OperatorNode} operatorNode The operatorNode we want to find in the terminals.
         */
        for (let i = 0; i < this.terminals.length; i++){
            if (this.terminals[i] === operatorNode){
                return i;
            }
        }
        return -1;
    }
    advance(){
        /**
         * Moves output produced by the operator to their designated terminal.
         */
        for (let i = 0; i < this.terminals; i++){
            this.terminals[i].addParams(this.outputs[i]);
        }
    }
}
