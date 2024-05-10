# fix-timeouts-discord
python code to fix the issue of members having metadata for being timed out when iterating through all timed out members within a server, even if their last timeout was from years prior
 
![cog currently includes 3 commands:](https://cdn.discordapp.com/attachments/1225711271761149972/1238396753447878767/image.png?ex=663f225a&is=663dd0da&hm=58814391f5fba6da6cecbbae1e8e2ed63ba47122a6f29cd4650ce87d7a3cecb5&)
- test command, to ensure cog is running properly
- `checktimers` command, to send list of all valid server timeouts, and print list of all expired/invalid ones
 - optionally, including a user argument will check if a specified user is timed out. if they have an expired timeout, it will print to the console instead
- `fixtimers` command, to iterate all server members with expired timeouts, re-time them out, then fix it-- thus deleting the metadata regarding them having a prior timeout period
 - WIP including optional user argument