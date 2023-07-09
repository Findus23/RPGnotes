It would be nice if colortheme.ts could be a part of the regular bundle.
But it needs to load as early as possible and blocking to avoid having white flashes in the dark theme.
Even using it in a seperate module that is loaded in the header doesn't work as modules are always deferred.

That's why it is built to a separate JS file by esbuild and hardcoded into the header.
