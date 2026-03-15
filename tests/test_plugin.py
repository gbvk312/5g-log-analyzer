

def test_plugin_import():
    from log_analyzer_plugin import LogAnalyzerPlugin

    plugin = LogAnalyzerPlugin()
    assert plugin.name == "log-analyzer"
