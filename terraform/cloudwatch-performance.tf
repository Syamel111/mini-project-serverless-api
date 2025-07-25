resource "aws_cloudwatch_metric_alarm" "high_invocation_count" {
  alarm_name          = "HighInvocationCount"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "Invocations"
  namespace           = "AWS/Lambda"
  period              = 60
  statistic           = "Sum"
  threshold           = 5
  alarm_description   = "Alarm when Lambda is invoked more than 5 times in a minute"
  dimensions = {
    FunctionName = "mini-api" # <-- Replace with your actual function name
  }
  alarm_actions = [aws_sns_topic.lambda_alerts.arn]
}

resource "aws_cloudwatch_metric_alarm" "high_duration" {
  alarm_name          = "HighLambdaDuration"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "Duration"
  namespace           = "AWS/Lambda"
  period              = 60
  statistic           = "Average"
  threshold           = 1000  # 1000ms = 1s
  alarm_description   = "Alarm when Lambda takes more than 1s"
  dimensions = {
    FunctionName = "MiniProject1Lambda" # <-- Replace with your function name
  }
  alarm_actions = [aws_sns_topic.lambda_alerts.arn]
}

resource "aws_cloudwatch_dashboard" "lambda_dashboard" {
  dashboard_name = "MiniProject1Dashboard"

  dashboard_body = jsonencode({
    widgets = [
      {
        type = "metric",
        x = 0,
        y = 0,
        width = 12,
        height = 6,
        properties = {
          metrics = [
            [ "AWS/Lambda", "Invocations", "FunctionName", "MiniProject1Lambda" ],
            [ ".", "Errors", ".", "." ],
            [ ".", "Duration", ".", ".", { "stat": "Average" } ]
          ],
          period = 60,
          stat = "Sum",
          region = "ap-southeast-1",
          title = "Lambda Metrics"
        }
      }
    ]
  })
}
