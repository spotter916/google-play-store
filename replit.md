# Overview

My Branches is a full-stack family collaboration web application with subscription tiers. Basic (free) users can create profiles and households can join groups to participate in tasks and events. Premium (paid) users can create groups, events, and access advanced planning features. The application provides a centralized platform for managing family relationships, organizing events, and facilitating communication across family networks.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: React 18 with TypeScript using Vite for development and build tooling
- **Routing**: Wouter for lightweight client-side routing
- **UI Components**: shadcn/ui component library built on Radix UI primitives
- **Styling**: Tailwind CSS with custom design system including color variables and theming
- **State Management**: TanStack Query (React Query) for server state management with optimistic updates
- **Forms**: React Hook Form with Zod validation for type-safe form handling
- **Real-time Communication**: WebSocket integration for live chat functionality

The frontend follows a component-based architecture with reusable UI components, custom hooks for business logic, and a clear separation between presentation and data fetching layers.

## Backend Architecture
- **Runtime**: Node.js with TypeScript and ESM modules
- **Framework**: Express.js for REST API endpoints
- **Database ORM**: Drizzle ORM with PostgreSQL dialect for type-safe database operations
- **Authentication**: Replit Auth integration using OpenID Connect with Passport.js
- **Session Management**: Express sessions stored in PostgreSQL using connect-pg-simple
- **Real-time Features**: WebSocket Server for group chat functionality
- **File Structure**: Monorepo structure with shared schema definitions between client and server

The backend implements a storage abstraction layer that encapsulates all database operations, making it easy to extend and maintain data access patterns.

## Database Design
- **Primary Database**: PostgreSQL with Neon serverless hosting
- **Schema Management**: Drizzle migrations with schema-first approach
- **Core Entities**: Users, Households, Groups, Events, Tasks, Messages with proper foreign key relationships
- **Session Storage**: Dedicated sessions table for authentication state
- **Data Validation**: Zod schemas shared between client and server for consistent validation

The database schema supports multi-tenancy through household groupings and flexible group memberships for different family structures.

## Authentication & Authorization
- **Provider**: Replit Auth using OpenID Connect protocol
- **Session Management**: Server-side sessions with PostgreSQL storage
- **Security**: HTTP-only cookies with secure flags and CSRF protection
- **User Management**: Automatic user creation/updates from OIDC claims with profile synchronization

## Real-time Communication
- **WebSocket Implementation**: Native WebSocket server for group chat
- **Message Broadcasting**: Room-based message distribution for group conversations
- **Connection Management**: Automatic reconnection handling and user presence tracking

# External Dependencies

## Database & Hosting
- **Neon Database**: Serverless PostgreSQL hosting with connection pooling
- **Replit Hosting**: Development and production environment with integrated authentication

## Authentication
- **Replit Auth**: OpenID Connect provider for user authentication and profile management

## UI & Styling
- **shadcn/ui**: Pre-built component library with Radix UI primitives
- **Tailwind CSS**: Utility-first CSS framework with custom design tokens
- **Lucide React**: Icon library for consistent iconography

## Development Tools
- **Vite**: Fast development server and build tool with HMR support
- **TypeScript**: Static type checking across the entire application
- **Drizzle Kit**: Database migration and schema management tools

## Mobile & PWA
- **Progressive Web App**: Installable mobile app experience with offline capabilities
- **Service Worker**: Background sync and caching for offline functionality
- **Responsive Design**: Mobile-first responsive layouts with touch-optimized navigation
- **App Store Ready**: Configuration for Google Play Store and Apple App Store deployment