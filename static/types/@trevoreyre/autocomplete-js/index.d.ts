// Type definitions for @trevoreyre/autocomplete 2.0
// Project: https://github.com/trevoreyre/autocomplete/, https://autocomplete.trevoreyre.com/
// Definitions by: versedi <https://github.com/versedi>
// Definitions: https://github.com/DefinitelyTyped/DefinitelyTyped
// TypeScript Version: 2.3
// from https://github.com/versedi/DefinitelyTyped/tree/trevoreyre/autocomplete-js/types/trevoreyre__autocomplete-js
declare module "@trevoreyre/autocomplete-js" {

// export as namespace Autocomplete;

    /**
     * Creates a props object with overridden toString function. toString returns an attributes
     * string in the format: `key1="value1" key2="value2"` for easy use in an HTML string.
     */
    export class Props {
        /**
         * @param index string
         * @param selectedIndex string
         * @param baseClass string
         */
        constructor(index: string, selectedIndex: string, baseClass: string);

        public toString(): string;
    }

// --------------------------------------------------------------------------------------
// Options Interfaces
// --------------------------------------------------------------------------------------

    export interface AutocompleteOptions {

        /**
         * Controls whether first result should be highlighted after input
         this.foo = val* Defaults to false, optional
         */
        autoSelect?: boolean;

        /**
         * The search function to be executed on user input. Can be a synchronous function or a Promise.
         * @param input
         */
        search(input: string): object | Promise<object>;

        /**
         * Sets the value of the calling component's input element
         */
        setValue?(): () => void;

        /**
         * Sets attributes on the calling component's input element
         */
        setAttribute?(): () => void;

        /**
         * Fired when the results list is updated. Receives results (Array), and selectedIndex (Number) as arguments.
         */
        onUpdate?(): () => void;

        /**
         * Fired when user submits result. Receives result as argument.
         * @param result
         */
        onSubmit(result: object): void;

        // getResultValue?(): (result:object) => string;
        getResultValue?: (result) => any

        /**
         *
         * @param result
         * @param props
         */
        renderResult?(result: object, props: Props): string;

        /**
         * Fired when the results list is shown
         */
        onShow?(): () => void;

        /**
         * Fired when the results list is hidden
         */
        onHide?(): () => void;

        /**
         * Fired if search is a Promise and hasn't resolved yet
         */
        onLoading?(): () => void;

        /**
         * Fired after asynchronous search function resolves
         */
        onLoaded?(): () => void;
    }

    export interface EventHandlers {
        handleInput: () => void;
        handleKeyDown: () => void;
        handleBlur: () => void;
        handleResultMouseDown: () => void;
        handleResultClick: () => void;
    }

// --------------------------------------------------------------------------------------
// Autocomplete
// --------------------------------------------------------------------------------------

    export default class Autocomplete<TElement = HTMLElement> {
        public options: AutocompleteOptions;

        constructor(inputSelector: string, options?: AutocompleteOptions);
    }

}
