export default class Operand {
    /**
     * Standard operand that is taken in a graph.
     */
    equals(operand){
        /**
         * Checks whether their memory addresses equal each other or not.
         * @param {Operand} operand Operand to compare to.
         */
        return this === operand;
    }
}
