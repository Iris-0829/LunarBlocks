export default class GraphTest{
    /**
     * Used for testing a given graph.
     * @param {GraphState} graph Graph to test on.
     */
    constructor(graph){
        this.graph = graph;
        this.input = []; // set manually
        this.hasStarted = false;
    }
    setInput(operandList){
        /**
         * Set input.
         * @param {Array} operandList list of operands to set in the inNode.
         */
        this.input = operandList;
    }
    step(){
        /**
         * Advances the operands in the graph.
         * @returns {boolean} true if a node has been executed, false otherwise.
         */
        // advance inNode
        if (!this.hasStarted){
            this.graph.inNode.params = this.input;
            this.graph.inNode.advance();
            this.hasStarted = true;
            return true;
        }
        // advance all operatorNodes if applicable
        else {
            for (let i = 0; i < this.graph.operatorNodes.length; i++){
                let executed = this.graph.operatorNodes[i].execute();
                if (executed){
                    this.graph.operatorNodes[i].advance()
                    return true;
                }
            }
        }
        return false;
    }
    getOutput(){
        /**
         * Gets output from the outNode.
         */
        return self.graph.outNode.execute();
    }
    reset(){
        /**
         * Resets the entire graph.
         */
        this.graph.inNode.params = []
        this.graph.outNode.params = []
        for (let i = 0; i < this.graph.operatorNodes.length; i++){
            this.graph.operatorNodes[i].params = []
            this.graph.operatorNodes[i].output = []
        }
        this.hasStarted = false;
    }
    autoTest(operandList){
        /**
         * Immediately returns the output of the testcase.
         * @param   {Array} operandList Input consisting of an array of operands.
         * @returns {Array} Output when given the following operandList.
         */
        this.reset()
        this.setInput(operandList)
        let running = true;
        while (running){
            running = this.step();
        }
        const out = this.getOutput();
        this.reset()
        return out;
    }
}