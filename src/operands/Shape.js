import Operand from 'Operand.js';

export default class Shape extends Operand {
    /**
     * A Shape operand.
     * @param {int} size Size of the shape.
     */
    constructor(size){
        super();
        this.size = size;
    }
    add(s){
        /**
         * Returns shape of the added sizes.
         * @param {Shape} s The size we want to add our own to create the new shape.
         */
        return Shape(this.size + s.size);
    }
    equals(s){
        /**
         * Checks whether their sizes are the same or not.
         * @param {Shape} s The shape we want to compare with.
         */
        return this.size === s.size;
    }
}