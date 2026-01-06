# Behave 測試執行腳本

# 執行所有測試
function Run-AllTests {
    Write-Host "🧪 執行所有測試..." -ForegroundColor Cyan
    behave
}

# 執行特定 scenario
function Run-Scenario {
    param([string]$Name)
    Write-Host "🎯 執行包含 '$Name' 的測試..." -ForegroundColor Cyan
    behave --name $Name
}

# 執行並生成 HTML 報告
function Run-WithReport {
    Write-Host "📊 執行測試並生成報告..." -ForegroundColor Cyan
    behave --format html --outfile test_report.html
    Write-Host "✅ 報告已生成: test_report.html" -ForegroundColor Green
}

# 快速冒煙測試
function Run-SmokeTest {
    Write-Host "🔥 執行冒煙測試..." -ForegroundColor Cyan
    behave --tags=@smoke
}

# 執行特定 feature
function Run-Feature {
    param([string]$FeatureName)
    Write-Host "📝 執行 $FeatureName..." -ForegroundColor Cyan
    behave "features/$FeatureName.feature"
}

# 除錯模式（詳細輸出 + 失敗停止）
function Run-Debug {
    Write-Host "🐛 除錯模式..." -ForegroundColor Yellow
    behave --verbose --stop --no-capture
}

# 顯示使用說明
function Show-Help {
    Write-Host @"
📖 Behave 測試執行腳本使用說明

可用函數：
  Run-AllTests              - 執行所有測試
  Run-Scenario "名稱"       - 執行特定 scenario
  Run-WithReport            - 執行測試並生成 HTML 報告
  Run-SmokeTest             - 執行冒煙測試
  Run-Feature "feature名"   - 執行特定 feature
  Run-Debug                 - 除錯模式執行

範例：
  Run-AllTests
  Run-Scenario "threshold"
  Run-Feature "order"
  Run-WithReport

"@ -ForegroundColor Green
}

# 顯示說明
Show-Help

