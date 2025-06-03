from venus import Venus

agent = Venus(tool_modules=['helpers'])

# agent auto creates claude mcp config and integrates tools from `file_operations` module
# anymore mcp server has helper tools and file operation tools
agent.build_mcp_server(configure_claude=True, modules=['file_operations']) 

if __name__ == '__main__':
  # run mcp server with cli transport
  agent.mcp.run(transport='stdio')
