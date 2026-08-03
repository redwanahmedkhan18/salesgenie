# Slack Service for SalesGenie

Production-ready Slack integration for AI-powered customer conversations, notifications, and workflows.

## Features

- **Real-time Messaging**: Send and receive messages through Slack channels and threads
- **Event Processing**: Handle Slack webhook events (messages, app mentions, reactions)
- **Channel Management**: Create and manage Slack channels programmatically
- **AI Assistant Integration**: Enable AI-powered responses in Slack channels
- **Rate Limiting**: Built-in rate limiting per channel

## API Endpoints

### Webhook
- `POST /api/v1/slack/webhook` - Receive Slack webhooks

### Channel Management
- `POST /api/v1/slack/workspace/{workspace_id}/channels` - Create a channel
- `POST /api/v1/slack/channels/{channel_id}/messages` - Send a message

### Integration Management
- `POST /api/v1/slack/integrations` - Register an integration
- `GET /api/v1/slack/integrations` - List integrations
- `GET /api/v1/slack/channels/{channel_id}` - Get integration details
- `DELETE /api/v1/slack/integrations/{channel_id}` - Remove integration

## Configuration

Set the following environment variables:
- `SLACK_SERVICE_PORT` (default: 8024)
- `SLACK_BOT_TOKEN` - Slack Bot User OAuth Token
- `SLACK_SIGNING_SECRET` - Signing secret for webhook verification

## Docker

```bash
docker build -t salesgenie/slack-service .
docker run -p 8024:8024 salesgenie/slack-service
```

## Database Migrations

Run the database migration to create required tables:
```bash
alembic upgrade head
```

Tables created:
- `slack_channel_integrations` - Slack channel configurations
- `discord_channel_integrations` - (shared) Channel integration metadata
- `channel_messages` - Unified message storage across all channels