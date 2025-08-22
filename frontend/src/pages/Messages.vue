<template>
  <div class="messages">
    <!-- Messages Header -->
    <div class="messages-header">
      <h1 class="page-title">Messages</h1>
    </div>

    <!-- Messages Layout -->
    <div class="messages-layout">
      <!-- Conversations Sidebar -->
      <div class="conversations-sidebar">
        <!-- Search Conversations -->
        <div class="search-container">
          <div class="search-box">
            <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
            </svg>
            <input 
              type="text" 
              v-model="searchQuery"
              placeholder="Search conversations..."
              class="search-input"
            >
          </div>
        </div>

        <!-- Conversations List -->
        <div class="conversations-list">
          <div 
            v-for="conversation in filteredConversations" 
            :key="conversation.id"
            @click="selectConversation(conversation)"
            class="conversation-item"
            :class="{ active: selectedConversation?.id === conversation.id }"
          >
            <div class="conversation-avatar">
              <span>{{ getInitials(conversation.contact.name) }}</span>
            </div>
            <div class="conversation-content">
              <div class="conversation-header">
                <h3 class="contact-name">{{ conversation.contact.name }}</h3>
                <span class="conversation-time">{{ formatTime(conversation.lastMessage.timestamp) }}</span>
              </div>
              <div class="conversation-preview">
                <p class="last-message">{{ conversation.lastMessage.text }}</p>
                <div v-if="conversation.unreadCount > 0" class="unread-badge">
                  {{ conversation.unreadCount }}
                </div>
              </div>
              <div class="contact-role">
                <span class="role-badge">{{ conversation.contact.role }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Chat Area -->
      <div class="chat-area">
        <div v-if="selectedConversation" class="chat-container">
          <!-- Chat Header -->
          <div class="chat-header">
            <div class="chat-contact-info">
              <div class="contact-avatar">
                <span>{{ getInitials(selectedConversation.contact.name) }}</span>
              </div>
              <div class="contact-details">
                <h3 class="contact-name">{{ selectedConversation.contact.name }}</h3>
                <p class="contact-role-desc">{{ selectedConversation.contact.roleDescription }}</p>
              </div>
            </div>
          </div>

          <!-- Messages Area -->
          <div class="messages-area" ref="messagesArea">
            <!-- Project Interest Header -->
            <div class="project-interest-header">
              <p class="interest-message">
                Hi! I'm very interested in your {{ selectedConversation.project.title }} project.
              </p>
              <span class="interest-date">{{ formatDate(selectedConversation.project.interestedDate) }}</span>
            </div>

            <!-- Messages -->
            <div v-for="message in selectedConversation.messages" :key="message.id" class="message-wrapper">
              <div 
                class="message" 
                :class="{ 
                  'sent': message.senderId === currentUserId, 
                  'received': message.senderId !== currentUserId 
                }"
              >
                <div class="message-content">
                  {{ message.text }}
                </div>
                <div class="message-time">
                  {{ formatTime(message.timestamp) }}
                </div>
              </div>
            </div>
          </div>

          <!-- Message Input -->
          <div class="message-input-container">
            <div class="message-input-box">
              <input 
                type="text" 
                v-model="newMessage"
                @keypress.enter="sendMessage"
                placeholder="Type your message..."
                class="message-input"
              >
              <button @click="sendMessage" class="send-button" :disabled="!newMessage.trim()">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
                </svg>
                Send
              </button>
            </div>
          </div>
        </div>

        <!-- No Conversation Selected -->
        <div v-else class="no-conversation">
          <div class="no-conversation-content">
            <div class="no-conversation-icon">💬</div>
            <h3 class="no-conversation-title">No conversation selected</h3>
            <p class="no-conversation-description">
              Select a conversation from the sidebar to start messaging
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Messages',
  data() {
    return {
      searchQuery: '',
      selectedConversation: null,
      newMessage: '',
      currentUserId: 'user1',
      conversations: [
        {
          id: 1,
          contact: {
            name: 'Alex Rodriguez',
            role: 'Developer',
            roleDescription: 'AI-Powered Personal Finance Assistant'
          },
          project: {
            title: 'AI-Powered Personal Finance Assistant',
            interestedDate: new Date('2024-02-10')
          },
          lastMessage: {
            text: 'I have experience with AI/ML integration and would love to discuss this project further.',
            timestamp: new Date('2024-02-10T15:30:00'),
            senderId: 'alex1'
          },
          unreadCount: 2,
          messages: [
            {
              id: 1,
              text: 'Great to hear from you! I\'d love to learn more about your experience with AI/ML.',
              timestamp: new Date('2024-02-10T14:30:00'),
              senderId: 'user1'
            },
            {
              id: 2,
              text: 'I have experience with AI/ML integration and would love to discuss this project further.',
              timestamp: new Date('2024-02-10T15:30:00'),
              senderId: 'alex1'
            }
          ]
        },
        {
          id: 2,
          contact: {
            name: 'David Kim',
            role: 'Developer',
            roleDescription: 'Smart Home IoT Hub'
          },
          project: {
            title: 'Smart Home IoT Hub',
            interestedDate: new Date('2024-02-09')
          },
          lastMessage: {
            text: 'The market potential for this project looks promising...',
            timestamp: new Date('2024-02-09T16:45:00'),
            senderId: 'david1'
          },
          unreadCount: 0,
          messages: [
            {
              id: 1,
              text: 'Hi David! Thanks for your interest in the IoT project.',
              timestamp: new Date('2024-02-09T16:00:00'),
              senderId: 'user1'
            },
            {
              id: 2,
              text: 'The market potential for this project looks promising. I\'d like to discuss the technical requirements.',
              timestamp: new Date('2024-02-09T16:45:00'),
              senderId: 'david1'
            }
          ]
        },
        {
          id: 3,
          contact: {
            name: 'Sarah Johnson',
            role: 'Investor',
            roleDescription: 'Healthcare Technology Investor'
          },
          project: {
            title: 'AI-Powered Health Monitoring',
            interestedDate: new Date('2024-02-08')
          },
          lastMessage: {
            text: 'I\'m interested in the healthcare applications. Can we schedule a call?',
            timestamp: new Date('2024-02-08T11:20:00'),
            senderId: 'sarah1'
          },
          unreadCount: 1,
          messages: [
            {
              id: 1,
              text: 'Hello Sarah! Thank you for your interest in our healthcare project.',
              timestamp: new Date('2024-02-08T10:30:00'),
              senderId: 'user1'
            },
            {
              id: 2,
              text: 'I\'m interested in the healthcare applications. Can we schedule a call?',
              timestamp: new Date('2024-02-08T11:20:00'),
              senderId: 'sarah1'
            }
          ]
        }
      ]
    }
  },
  computed: {
    filteredConversations() {
      if (!this.searchQuery) return this.conversations
      
      return this.conversations.filter(conversation =>
        conversation.contact.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        conversation.contact.role.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        conversation.lastMessage.text.toLowerCase().includes(this.searchQuery.toLowerCase())
      )
    }
  },
  mounted() {
    // Auto-select first conversation
    if (this.conversations.length > 0) {
      this.selectedConversation = this.conversations[0]
    }
  },
  methods: {
    selectConversation(conversation) {
      this.selectedConversation = conversation
      // Mark as read
      conversation.unreadCount = 0
      this.$nextTick(() => {
        this.scrollToBottom()
      })
    },
    
    sendMessage() {
      if (!this.newMessage.trim() || !this.selectedConversation) return
      
      const message = {
        id: Date.now(),
        text: this.newMessage.trim(),
        timestamp: new Date(),
        senderId: this.currentUserId
      }
      
      this.selectedConversation.messages.push(message)
      this.selectedConversation.lastMessage = {
        text: message.text,
        timestamp: message.timestamp,
        senderId: message.senderId
      }
      
      this.newMessage = ''
      
      this.$nextTick(() => {
        this.scrollToBottom()
      })
    },
    
    scrollToBottom() {
      if (this.$refs.messagesArea) {
        this.$refs.messagesArea.scrollTop = this.$refs.messagesArea.scrollHeight
      }
    },
    
    getInitials(name) {
      return name.split(' ').map(n => n[0]).join('').slice(0, 2)
    },
    
    formatTime(date) {
      if (!date) return ''
      return new Intl.DateTimeFormat('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      }).format(new Date(date))
    },
    
    formatDate(date) {
      if (!date) return ''
      return new Intl.DateTimeFormat('en-US', {
        month: 'short',
        day: 'numeric'
      }).format(new Date(date))
    }
  }
}
</script>

<style scoped>
.messages {
  max-width: 1400px;
  margin: 0 auto;
  height: calc(100vh - 140px);
}

.messages-header {
  margin-bottom: 1.5rem;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
}

.messages-layout {
  display: grid;
  grid-template-columns: 350px 1fr;
  gap: 0;
  height: calc(100vh - 200px);
  background: white;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

/* Conversations Sidebar */
.conversations-sidebar {
  border-right: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
}

.search-container {
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
}

.search-box {
  position: relative;
}

.search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 0.5rem 0.75rem 0.5rem 2.5rem;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  font-size: 0.875rem;
}

.search-input:focus {
  outline: none;
  border-color: #667eea;
}

.conversations-list {
  flex: 1;
  overflow-y: auto;
}

.conversation-item {
  padding: 1rem;
  border-bottom: 1px solid #f3f4f6;
  cursor: pointer;
  transition: background-color 0.2s ease;
  display: flex;
  gap: 0.75rem;
}

.conversation-item:hover {
  background-color: #f9fafb;
}

.conversation-item.active {
  background-color: #eef2ff;
  border-right: 3px solid #667eea;
}

.conversation-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
  flex-shrink: 0;
}

.conversation-content {
  flex: 1;
  min-width: 0;
}

.conversation-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.25rem;
}

.contact-name {
  font-weight: 600;
  color: #1a202c;
  font-size: 0.875rem;
  margin: 0;
}

.conversation-time {
  color: #6b7280;
  font-size: 0.75rem;
}

.conversation-preview {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.last-message {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex: 1;
}

.unread-badge {
  background: #ef4444;
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.125rem 0.375rem;
  border-radius: 10px;
  min-width: 18px;
  text-align: center;
}

.role-badge {
  background: #f3f4f6;
  color: #374151;
  padding: 0.125rem 0.5rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

/* Chat Area */
.chat-area {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.chat-header {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  background: #f9fafb;
}

.chat-contact-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.contact-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1rem;
}

.contact-details .contact-name {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0 0 0.25rem 0;
}

.contact-role-desc {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}

.messages-area {
  flex: 1;
  padding: 1rem 1.5rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.project-interest-header {
  text-align: center;
  padding: 1rem;
  background: #eef2ff;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.interest-message {
  color: #4338ca;
  font-weight: 500;
  margin: 0 0 0.5rem 0;
}

.interest-date {
  color: #6b7280;
  font-size: 0.875rem;
}

.message-wrapper {
  display: flex;
  margin-bottom: 1rem;
}

.message.sent {
  margin-left: auto;
}

.message.received {
  margin-right: auto;
}

.message {
  max-width: 70%;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.message-content {
  padding: 0.75rem 1rem;
  border-radius: 18px;
  word-wrap: break-word;
}

.message.sent .message-content {
  background: #667eea;
  color: white;
  border-bottom-right-radius: 4px;
}

.message.received .message-content {
  background: #f3f4f6;
  color: #1a202c;
  border-bottom-left-radius: 4px;
}

.message-time {
  font-size: 0.75rem;
  color: #9ca3af;
  padding: 0 0.5rem;
}

.message.sent .message-time {
  text-align: right;
}

.message-input-container {
  padding: 1rem 1.5rem;
  border-top: 1px solid #e5e7eb;
  background: white;
}

.message-input-box {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.message-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 24px;
  font-size: 0.875rem;
}

.message-input:focus {
  outline: none;
  border-color: #667eea;
}

.send-button {
  background: #667eea;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 24px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: background-color 0.2s ease;
}

.send-button:hover:not(:disabled) {
  background: #5a67d8;
}

.send-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.send-button svg {
  width: 16px;
  height: 16px;
}

.no-conversation {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.no-conversation-content {
  text-align: center;
  max-width: 300px;
}

.no-conversation-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.no-conversation-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0 0 0.5rem 0;
}

.no-conversation-description {
  color: #6b7280;
  margin: 0;
}

@media (max-width: 768px) {
  .messages-layout {
    grid-template-columns: 1fr;
    height: auto;
  }
  
  .conversations-sidebar {
    display: none;
  }
  
  .page-title {
    font-size: 2rem;
  }
}
</style>