import OperatorNode from 'OperatorNode.js';

class AdditionNode extends OperatorNode{
    /**
     * Node that does binary addition between two operands when executed.
     */
    constructor(){
        super(2);
    }
    execute(){
        /**
         * Attempts to execute the operator with the given terminals.
         */
        if (self.params.length === self.numPorts){
            self.output = [self.params[0].add(self.params[1])];
        }
    }
}
