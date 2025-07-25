resource "aws_cloudwatch_log_metric_filter" "lambda_error_filter" {
  name           = "LambdaErrorFilter"
  log_group_name = "/aws/lambda/${var.lambda_function_name}"

  pattern = "\"ERROR\""

  metric_transformation {
    name      = "LambdaErrorCount"
    namespace = "MiniProjectMetrics"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "lambda_error_alarm" {
  alarm_name          = "LambdaErrorAlarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = aws_cloudwatch_log_metric_filter.lambda_error_filter.metric_transformation[0].name
  namespace           = aws_cloudwatch_log_metric_filter.lambda_error_filter.metric_transformation[0].namespace
  period              = 60
  statistic           = "Sum"
  threshold           = 1

  alarm_description   = "Triggered when Lambda logs contain 'ERROR'"
  alarm_actions       = [aws_sns_topic.lambda_alerts.arn]

  depends_on = [aws_cloudwatch_log_metric_filter.lambda_error_filter]
}
