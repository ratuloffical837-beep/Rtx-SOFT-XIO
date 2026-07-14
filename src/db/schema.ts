import { pgTable, serial, text, integer, timestamp, doublePrecision, jsonb, boolean } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  telegramId: text("telegram_id").primaryKey(),
  username: text("username"),
  firstName: text("first_name"),
  language: text("language").default("en"),
  balanceUsdt: doublePrecision("balance_usdt").default(0),
  balanceTon: doublePrecision("balance_ton").default(0),
  balanceUsdc: doublePrecision("balance_usdc").default(0),
  balanceRtx: doublePrecision("balance_rtx").default(0),
  miningMultiplier: doublePrecision("mining_multiplier").default(1.0),
  currentStreak: integer("current_streak").default(0),
  lastClaimDate: timestamp("last_claim_date"),
  completedTasks: jsonb("completed_tasks").default([]),
  referredBy: text("referred_by"),
  referralCount: integer("referral_count").default(0),
  totalRtxEarned: doublePrecision("total_rtx_earned").default(0),
  createdAt: timestamp("created_at").defaultNow(),
  lastSyncedAt: timestamp("last_synced_at").defaultNow()
});

export const p2pListings = pgTable("p2p_listings", {
  id: serial("id").primaryKey(),
  ownerId: text("owner_id").references(() => users.telegramId),
  ownerUsername: text("owner_username"),
  type: text("type"), // 'buy' | 'sell'
  rtxAmount: doublePrecision("rtx_amount"),
  pricePerRtx: doublePrecision("price_per_rtx"),
  paymentMethods: jsonb("payment_methods").default([]),
  status: text("status").default("active"), // 'active' | 'completed' | 'cancelled'
  createdAt: timestamp("created_at").defaultNow()
});

export const transactions = pgTable("transactions", {
  id: serial("id").primaryKey(),
  senderId: text("sender_id"),
  receiverId: text("receiver_id"),
  amount: doublePrecision("amount"),
  type: text("type"), // 'transfer' | 'withdrawal' | 'reward' | 'boost_purchase'
  status: text("status").default("pending"),
  createdAt: timestamp("created_at").defaultNow()
});

export const withdrawalRequests = pgTable("withdrawal_requests", {
  id: serial("id").primaryKey(),
  userId: text("user_id").references(() => users.telegramId),
  currency: text("currency"),
  amount: doublePrecision("amount"),
  walletAddress: text("wallet_address"),
  network: text("network"),
  status: text("status").default("pending"),
  createdAt: timestamp("created_at").defaultNow()
});

export const boostRequests = pgTable("boost_requests", {
  id: serial("id").primaryKey(),
  userId: text("user_id").references(() => users.telegramId),
  tonAmount: doublePrecision("ton_amount"),
  txid: text("txid"),
  status: text("status").default("pending"),
  boostMultiplier: doublePrecision("boost_multiplier").default(1.0),
  createdAt: timestamp("created_at").defaultNow()
});

export const cpaTransactions = pgTable("cpa_transactions", {
  transactionId: text("transaction_id").primaryKey(),
  userId: text("user_id").references(() => users.telegramId),
  amount: doublePrecision("amount"),
  userAmount: doublePrecision("user_amount"),
  adminAmount: doublePrecision("admin_amount"),
  currency: text("currency"),
  processedAt: timestamp("processed_at").defaultNow()
});

export const adminStats = pgTable("admin_stats", {
  id: serial("id").primaryKey(),
  totalCPALeadProfit: doublePrecision("total_cpalead_profit").default(0),
  totalBoostRevenue: doublePrecision("total_boost_revenue").default(0),
  pendingWithdrawals: integer("pending_withdrawals").default(0),
  weeklyRtxDistributed: doublePrecision("weekly_rtx_distributed").default(0),
  lastUpdated: timestamp("last_updated").defaultNow()
});
