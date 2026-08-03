# Discord Service for SalesGenie

Production-ready Discord integration for AI-powered customer conversations, notifications, and workflows.

## Features

- **Real-time Messaging**: Send and receive messages through Discord channels
- **Interaction Handling**: Process Discord interactions (slash commands, message components)
- **Channel Management**: Create and manage Discord text channels
- **AI Assistant Integration**: Enable AI-powered responses in Discord channels
- **Bot Invitation**: Generate invite links for your Discord bot

## API Endpoints

### Webhook
- `POST /api/v1/discord/webhook` - Receive Discord webhooks/interactions

### Channel Management
- `POST /api/v1/discord/workspaces/{guild_id}/channels` - Create a channel
- `POST /api/v1/discord/channels/{channel_id}/messages` - Send a message

### Integration Management
- `POST /api/v1/discord/integrations` - Register an integration
- `GET /api/v1/discord/integrations` - List integrations
- `GET /api/v1/discord/channels/{channel_id}` - Get integration details
- `DELETE /api/v1/discord/integrations/{channel_id}` - Remove integration
- `POST /api/v1/discord/bots/{guild_id}/invite` - Generate bot invite URL

## Configuration

Set the following environment variables:
- `DISCORD_SERVICE_PORT` (default: 8026)
- `DISCORD_BOT_TOKEN` - Discord Bot User OAuth2 Token

## Docker

```bash
docker build -t salesgenie/discord-service .
docker run -p 8026:8026 salesgenie/discord-service
```

## Database Migrations

Run the database migration to create required tables:
```bash
alembic upgrade head
```

Tables created:
- `discord_channel_integrations` - Discord channel configurations
- `channel_messages` - Unified message storage across all channels

## Permissions

For the bot to function properly, it needs these permissions:
- Send Messages (0x00000800)
- Read Message History (0x000010000)
- Add Reactions (0x00004000)
- Use Slash Commands (0x000080000000)